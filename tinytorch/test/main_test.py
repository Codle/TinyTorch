
import numpy as np

import tinytorch
import tinytorch.functional as F
import tinytorch.nn as nn


class MLP(nn.Module):

    def __init__(self, h1, h2, h3):
        self.linear1 = nn.Linear(h1, h2)
        self.linear2 = nn.Linear(h2, h3)

    def forward(self, x):
        out = self.linear1(x)
        out = F.sigmoid(out)
        out = self.linear2(out)
        return out

