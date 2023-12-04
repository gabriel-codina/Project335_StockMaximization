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
      result = total_stocks(exhaustive_opt_stocks(stock_list,max_budget))
      print(result)
      results.append(result)
  write_to_output(results)

def exhaustive_opt_stocks(stock_list, max_budget):
  #using exhaustive optimization algorithm to find the best combination of stocks
  best = None
  for candidate in combos(stock_list):
    if verify_price(max_budget, candidate):
      if best is None or total_stocks(candidate) > total_stocks(best):
        best = candidate
  return best

def total_stocks(candidate):
  #get the total number of stocks in the candidate
  total=0
  for item in candidate:
    total+=item[0]
  return total

def verify_price(max_budget, candidate):
  #verify if the total price of the candidate is less than the max budget
  total=0
  for item in candidate:
    total+=item[1]
  if total>max_budget:
    return False
  return True

def combos(stock_list):
  #generate all possible combinations of stocks
  combos = []
  for i in range(len(stock_list)):
    combos.extend(list(itertools.combinations(stock_list,i+1)))
  return combos

def write_to_output(results):
  with open("output_a.txt", "w") as output_a:
    for i in results:
      output_a.write(str(i) + "\n")

if __name__ == "__main__":
  main()
