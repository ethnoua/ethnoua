# Description

Installs the [Geospatial Data Abstraction Library (GDAL)](http://www.gdal.org/).

## Platforms:

Tested on:

* Ubuntu 12.04

## Recipes:

* `default.rb` - Downloads, builds, and installs GDAL from source.

## Attributes

* `node['gdal']['version']` - the version of GDAL to use.


## TODO

* add custom attribute for `install_url`
* support multiply versions of gdal installed
* buid options

License and Author
==================

Author:: Vasyl Dizhak (<dijakroot@gmail.com>)

Copyright:: 2013, Django Stars LLC.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

