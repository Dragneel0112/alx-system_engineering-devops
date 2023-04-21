# Pip3 install flask v2.1.0, Using Puppet
package { 'flask':
  ensure   =>  '2.1.0',
  provider =>  'pip3'
}
