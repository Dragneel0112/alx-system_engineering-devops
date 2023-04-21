# Pip3 install flask v2.1.0, Using Puppet
package { 'flask':
  ensure          =>  'installed',
  provider        =>  'pip3'
  install_options =>  ['-v', '2.1.0'],
}
