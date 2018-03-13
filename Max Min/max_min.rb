#!/bin/ruby

def angryChildren(k, arr)
  arr.sort.each_cons(k).map { |x| x[-1]-x[0] }.min
end

n = gets.strip.to_i
k = gets.strip.to_i
arr = Array.new(n)
(0...n).each do |i|
  arr[i] = gets.strip.to_i
end
result = angryChildren(k, arr)
puts result
