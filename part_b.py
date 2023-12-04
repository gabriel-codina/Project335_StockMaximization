import itertools
import ast

def main():
  line_count = 0
  max_budget=0
  stock_list=[]
  
  f = open("input_b.txt", "r")
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
    n = len(stock_list)
    dp = [[0] * (max_budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(max_budget + 1):
            dp[i][j] = dp[i - 1][j]
            if stock_list[i - 1][1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - stock_list[i - 1][1]] + stock_list[i - 1][0])

    # finding the optimal combination of stocks through backtracking
    solution = []
    while n and max_budget > 0:
        if dp[n][max_budget] != dp[n - 1][max_budget]:
            solution.append(stock_list[n - 1])
            max_budget -= stock_list[n - 1][1]
        n -= 1

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
