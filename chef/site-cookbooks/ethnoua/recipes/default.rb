#
# Cookbook Name:: ethnoua
# Recipe:: default
#
# Copyright 2013,  Vasyl Dizhak
#

include_recipe 'python'

package "vim"
package "screen"


python_virtualenv "/home/vagrant/envs/ethnoua_env" do
  owner "vagrant"
  group "vagrant"
  options "--no-site-packages"
  action :create
end

script "install_ethnoua_python_package" do
  interpreter "bash"
  user "vagrant"
  cwd "/vagrant/"
  code <<-EOH
  /home/vagrant/envs/ethnoua_env/bin/python setup.py develop
  EOH
end
