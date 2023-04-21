# Pip3 install flask v2.1.0, with Puppet
package { 'flask from pip3':
  ensure          =>  'installed',
  install_options =>  ['-v', '2.1.0'],
}
