# Copyright 2024 The Flax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from .module import ModuleMeta as ModuleMeta
from .module import Module as Module
from .module import Scope as Scope
from .module import compact as compact
from .wrappers import functional as functional
from .wrappers import Functional as Functional
from .wrappers import ToNNX as ToNNX
from .wrappers import lazy_init as lazy_init
from .wrappers import ToLinen as ToLinen
from .wrappers import to_linen as to_linen
from .variables import NNXMeta as NNXMeta
from .variables import register_variable_name_type_pair as register_variable_name_type_pair