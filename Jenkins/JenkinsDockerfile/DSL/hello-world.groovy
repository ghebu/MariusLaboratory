folder('tests') { 
  displayName('tests')
  description('DSL jobs sandbox')
}
job('tests/example') {
  steps {
    shell('echo Hello World!')
  }
}