n = int(input("Enter the number of stones: "))

def stone_piles(n):
  piles = []
    
  if n % 2 == 0: 
    pile = 2 # if even all piles should have even only
  else:
    pile = 1 # if odd all piles should have odd only
        
  while sum(piles) + pile <= n:
    piles.append(pile)
    pile += 2
    
  return piles

result = stone_piles(n)
print(f"Stones in a single pile = {result}")