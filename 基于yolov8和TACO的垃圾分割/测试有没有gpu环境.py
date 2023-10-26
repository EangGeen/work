import torch
import os
print(torch.cuda.is_available())
print(os.environ.get('CUDA_VISIBLE_DEVICES'))
print(torch.cuda.device_count())
print(torch.__version__)
print(torch.zeros(1).cuda())

