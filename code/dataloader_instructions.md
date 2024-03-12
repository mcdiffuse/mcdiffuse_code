This is a generalized dataloader we created that the training script uses. All that is required for initialization is a `metadata.json` file formatted like the one included here and specific folder names.

Your structure should resemble this
```
\ Root folder
---\ metadata.json
---\ mixture
------\mixture_0.flac
------\mixture_1.flac
------\mixture_2.flac
---\ s1
------\mixture_0.flac
------\mixture_1.flac
------\mixture_2.flac
```
Importantly the names of each file must match the `"mix_id"` in the json list.