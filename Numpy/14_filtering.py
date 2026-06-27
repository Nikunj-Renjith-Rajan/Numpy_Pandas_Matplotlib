#Filtering an array for a given condition
import numpy as np

ages=np.array([11,17,18,23,29,39,43,57,62,67,80])
teenagers=ages[ages<18]
adults=ages[(ages>=18) & (ages<=65)]
seniors=ages[ages>65]
not_eligible=ages[(ages<18) | (ages>65)]
evens=ages[ages%2==0]
odds=ages[ages%2!=0]

print(teenagers)
print(adults)
print(seniors)
print(not_eligible)
print(evens)
print(odds)

#////////////////////////////////////WHERE FUNCTION//////////////////////////////////////////
# with the help of where function, we can filter an array along with
# preserving its initial shape, by replacing the filtered-out elements with
# a desired value
#          SYNTAX: np.where(filter_condition,array_name,value_to_be_replaced_with)

a=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.where(a%2==0,a,-1))