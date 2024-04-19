# install flask

package { 'flask':
  ensure   => '3.0.3',
  provider => 'pip3',
}
