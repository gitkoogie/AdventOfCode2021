import time

start = time.perf_counter()
def get_input():
   with open('inputs/day4.txt') as f:
      temp = f.readlines()

   # fix input
   # seq
   seq = temp[0].split(",")
   seq[-1] = seq[-1].strip("\n")

   # boards
   boards = []
   row = 0
   t1 = []

   lines = []
   for i in range(1, len(temp)):
      if temp[i] != "\n":
         lines.append(temp[i].strip("\n"))

   lines2 = []
   for i in range(len(lines)):
      lines2.append(lines[i].split(" "))

   lines = []
   for i in range(len(lines2)):
      lines.append(list(filter(lambda a: a != "", lines2[i])))

   boards = []
   row = 0
   t = []
   for i in range(len(lines)):
      t.append(lines[i])
      row += 1

      if row == 5:
         row = 0
         boards.append(t)
         t = []
   return seq, boards


def check_bingo(boards, bingos):
   for board in range(len(boards)):
      found = []
      count = [0, 0, 0, 0, 0]
      for row in range(len(boards[board])):
         indices = [i for i, x in enumerate(boards[board][row]) if x == -1]
         if indices:
            found.extend([row, indices])
      if found:
         for i in range(len(found)):
            # if bingo on row
            if found[i] == [0, 1, 2, 3, 4]:
               if board not in bingos:
                  bingos.append(board)

            elif isinstance(found[i], int):
               if found[i] == 0:
                  count[0] += 1
               elif found[i] == 1:
                  count[1] += 1
               elif found[i] == 2:
                  count[2] += 1
               elif found[i] == 3:
                  count[3] += 1
               elif found[i] == 4:
                  count[4] += 1
         # if -1 on each row
         if count == [1, 1, 1, 1, 1]:
            cnt = [0, 0, 0, 0, 0]
            for i in range(len(found)):
               if type(found[i]) is list:
                  for j in range(len(found[i])):
                     if found[i][j] == 0:
                        cnt[0] += 1
                     if found[i][j] == 1:
                        cnt[1] += 1
                     if found[i][j] == 2:
                        cnt[2] += 1
                     if found[i][j] == 3:
                        cnt[3] += 1
                     if found[i][j] == 4:
                        cnt[4] += 1
            if [i for i, x in enumerate(cnt) if x == 5]:
               if board not in bingos:
                  bingos.append(board)
   return bingos

def compute_score(board, nr):
   # count number of highlighted
   minus_ones = 0
   for row in range(len(board)):
      minus_ones += len([i for i, x in enumerate(board[row]) if x == -1])
   # compute sum of not highlighted
   summ_noH = 0
   for row in range(len(board)):
      for val in range(len(board[row])):
         summ_noH += int(board[row][val])
   summ_noH = summ_noH + minus_ones
   return summ_noH * nr


def day4part1():
   seq, boards = get_input()
   bingos = []
   for i in range(len(seq)):
      # assert bingo values to -1
      for j in range(len(boards)):
         for r in range(len(boards[j])):
            for val in range(len(boards[j][r])):
               if seq[i] == boards[j][r][val]:
                  boards[j][r][val] = -1

      # check for bingo
      bingos = check_bingo(boards, bingos)
      if bingos:
         # compute score
         result = compute_score(boards[bingos[0]], int(seq[i]))
         return result

def compute_score2(seq, board, nr):
   for i in range(len(seq)):
      # assert bingo values to -1
      for r in range(len(board)):
         for val in range(len(board[r])):
            if seq[i] == board[r][val]:
               board[r][val] = -1
   
      if seq[i] == nr:
         break
   return compute_score(board, int(nr))


def day4part2():
   winners = []
   count = 0
   bingos = []
   seq, boards = get_input()
   for i in range(len(seq)):
      # assert bingo values to -1
      for j in range(len(boards)):
         for r in range(len(boards[j])):
            for val in range(len(boards[j][r])):
               if seq[i] == boards[j][r][val]:
                  boards[j][r][val] = -1

      # check for bingo
      l = len(bingos)
      bingos = check_bingo(boards, bingos)
      
      if len(bingos) > l:
         curr_val = seq[i]

   seq, init_boards = get_input()
   return compute_score2(seq, init_boards[bingos[-1]], curr_val)


print(day4part1())
print(day4part2())
print((time.perf_counter() - start)*1000, "ms")