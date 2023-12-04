import itertools
import ast

def main():
  line_count = 0
  max_budget=0
  stock_list=[]
  
  f = open("input_project2.txt", "r")
  results = []
  for x in f:
    #split input in 3 lines(# of stocks, stock_list, and max_budget)
    if line_count==0 and x.strip().isdigit():
      line_count+=1
    elif line_count==1:
      line_count+=1
      stock_list = ast.literal_eval(x) #parses the string into a list
    elif line_count==2:
      line_count=0
      max_budget=int(x)
      result = total_stocks(dynamic_opt_stocks(stock_list,max_budget))
      print(result)
      results.append(result)
    write_to_output(results)


def dynamic_opt_stocks(stock_list, max_budget):
  #using a dynamic algorithm to find the best combination of stocks
  solution=[]
  #evaluate stock value and add it as a third item
  for stock in stock_list:
    stock.append(stock[0]/stock[1])
  #while their is items in our list and we still have a budget get the highest value stock option
  while stock_list and max_budget > 0:
    best_val_option=max(stock_list, key=lambda x: x[2])#get highest value set
    if best_val_option[1]<=max_budget:
      solution.append([best_val_option[0],best_val_option[1]])
      max_budget-=best_val_option[1]
    stock_list.remove(best_val_option)
  return solution

def total_stocks(candidate):
  #get the total number of stocks in the candidate
  total=0
  for item in candidate:
    total+=item[0]
  return total

def write_to_output(results):
  with open("output_b.txt", "w") as output_b:
    for i in results:
      output_b.write(str(i) + "\n")


if __name__ == "__main__":
  main()
