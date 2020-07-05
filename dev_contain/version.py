#
# Copyright 2019 James Pace
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

def version():
    file_path = os.path.dirname(os.path.abspath(__file__))

    version_lines = ['']
    with open(os.path.join(file_path, 'version.yaml'), 'r') as f:
        version_lines = f.readlines()

    for line in version_lines:
        print(line.strip())

if __name__ == '__main__':
    version()
