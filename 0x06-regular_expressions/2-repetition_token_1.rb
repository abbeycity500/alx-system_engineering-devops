#!/usr/bin/env ruby
# A ruby script that accept one argument and pass it to a rgex matching method
puts ARGV[0].scan(/hb?tn/).join
