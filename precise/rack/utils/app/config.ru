$LOAD_PATH << File.expand_path("lib")
require 'helloworld '

map "/" do
  run HelloWorld
end
