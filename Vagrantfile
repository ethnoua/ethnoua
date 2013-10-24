# -*- mode: ruby -*-
# vi: set ft=ruby :


VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "u12.04-ethnoua"

  config.vm.box_url = "https://s3-eu-west-1.amazonaws.com/chef-boxes-img/ubuntu/package.box"

  config.vm.network :forwarded_port, guest: 80, host: 8081

  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = ["./chef/site-cookbooks", "./chef/cookbooks"]
    chef.roles_path = "./chef/roles"
    chef.data_bags_path = "./chef/data_bags"
    chef.add_role "dev"
  end

end
