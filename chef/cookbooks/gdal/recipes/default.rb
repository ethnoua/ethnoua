gdal_version = node['gdal']['version']

ark "gdal" do
  url "http://download.osgeo.org/gdal/#{gdal_version}/gdal-#{gdal_version}.tar.gz"
  version gdal_version
  action [:configure, :install_with_make]
  creates "/usr/local/gdal-#{gdal_version}"
end
