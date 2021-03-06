import torch.nn as nn
import pretrainedmodels
import torch.nn.functional as F


class ResNet18(nn.Module):
    def __init__(self, pretrained):
        super(ResNet18, self).__init__()
        if pretrained is True:
            self.model = pretrainedmodels.__dict__["resnet18"](
            pretrained = "imagenet")
        else:
            self.model = pretrainedmodels.__dict__["resnet18"](
            pretrained = None)
        # TODO(Sayar): Modify last layer of network to include classes to predict

    def forward(self):
        # TODO(Sayar): Add forward pass logic
        pass
