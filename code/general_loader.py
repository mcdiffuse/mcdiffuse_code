import glob
import json
import os
from pathlib import Path
import asteroid_filterbanks.transforms as af_transforms
import numpy as np
import torch
from torch.utils.data import Dataset
import soundfile as sf
from torchaudio import load as tload


class General_Loader(Dataset):
    def __init__(
        self,
        dset_root,
        samplerate=16_000,
        nfft=512,
        hop_length=128,
        length = 8,
    ):
        self.dset_root = dset_root
        self.conf_file = os.path.join(dset_root, "metadata.json")
        self.data = self.get_metadata(self.conf_file)
        self.samplerate = samplerate
        self.nfft = nfft
        self.hop_length = hop_length
        self.length = length
        self.wav_length = int(length * samplerate)
        print(dset_root)
    
    
    def get_metadata(self, json_path = "metadata.json"):
        with open(json_path) as f:
            data = json.load(f)
        return data
    
    def _read_wave(self, file):

        audio, fs = tload(file)        

        audio_std = torch.std(audio, dim=-1, keepdim=True)
        audio = audio / (audio_std + 1e-8)

        assert fs == self.samplerate
        return audio
        
    def _compute_stft(self, mixture):
        cstft = torch.stft(
            mixture, 
            n_fft=self.nfft,
            hop_length=self.hop_length,
            win_length=self.nfft,
            window=torch.hann_window(self.nfft)**0.5,
            center=True,  # Typically, centering helps with signal reconstruction
            pad_mode='reflect',
            normalized=False,
            onesided=True,  # True for real-valued signals
            return_complex=True
        )
        return cstft
    
    def _invert_stft(self, cstft):
        reconstructed_signal = torch.istft(
            cstft, 
            n_fft=self.nfft,
            hop_length=self.hop_length,
            win_length=self.nfft,
            window=torch.hann_window(self.nfft)**0.5,
            center=True,  # Should match the setting in compute_stft
            normalized=False,
            onesided=True,  # True for real-valued signals
            length=None,  # You can specify the original signal length if known
            return_complex=False
        )
        return reconstructed_signal
    
    def _scale_stft(self, cstft):
        mag, phase = af_transforms.magphase(af_transforms.from_torch_complex(cstft))
        mag = mag**(0.5)/6
        cstft = af_transforms.from_magphase(mag, phase)
        return af_transforms.to_torch_complex(cstft)

    def _iscale_stft(self, cstft):
        # invert scaling
        mag, phase = af_transforms.magphase(
            af_transforms.from_torch_complex(cstft))
        mag = (mag*6)**2
        cstft = af_transforms.from_magphase(mag, phase)
        return af_transforms.to_torch_complex(cstft)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, item):
                
        datum = self.data[item]
                
        s1_path = os.path.join(self.dset_root, "s1", datum['mix_id']+".flac")
        
        mix_path = os.path.join(self.dset_root, "mixture", datum['mix_id']+".flac")
        
            
            
        # print(s1_path)
        # print(mix_path)
        s1 = self._read_wave(s1_path)
        mix = self._read_wave(mix_path)

        if mix.dim() == 2:
            mix = mix[0, :]
            
        if s1.dim() == 2:
            s1 = s1[0, :]

        
        
        s1_spec = self._compute_stft(s1)
        
        mix_spec = self._compute_stft(mix)
                
        def cat_reim(cstft):
            return torch.stack((cstft.real, cstft.imag), 0)
        s1_spec = cat_reim(self._scale_stft(s1_spec))
        mix_spec = cat_reim(self._scale_stft(mix_spec))
        
        
        return {
            "mixture": mix_spec,
            "sources": s1_spec,
            "noise": None,
            "wav": [s1, mix, None],
            "filename": [s1_path, mix_path],
            "metadata": datum,
            "std": [s1.std(), mix.std()]
        }