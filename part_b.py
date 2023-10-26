import itertools
import ast

def main():
  line_count = 0
  max_budget=0
  stock_list=[]
  
  f = open("input_project2.txt", "r")
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
      print(total_stocks(dynamic_opt_stocks(stock_list,max_budget)))

def dynamic_opt_stocks(stock_list, max_budget):
  #using a dynamic algorithm to find the best combination of stocks
  
  return None

#probably wont need
def total_stocks(candidate):
  #get the total number of stocks in the candidate
  total=0
  for item in candidate:
    total+=item[0]
  return total



if __name__ == "__main__":
  main()
