#
# Cookbook Name:: ethnoua
# Recipe:: default
#
# Copyright 2013,  Vasyl Dizhak
#

include_recipe 'python'
include_recipe 'nvm'

package "vim"
package "screen"
package "htop"
package "tmux"


directory '/home/vagrant/.tmuxinator' do
  owner "vagrant"
  group "vagrant"
  action :create
end

template '/home/vagrant/.tmuxinator/ethnoua.yml' do 
  source "tmuxinator_ethnoua.yml"
  owner "vagrant"
  group "vagrant"
end

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


nvm_install '0.10.21'  do
    from_source false
    alias_as_default true
    action :create
end
