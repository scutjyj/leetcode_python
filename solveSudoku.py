class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        self.tl = []
        tl_p = self.find_next_dot(-1, self.tl, board)
        #self.iter_func(tl_p, self.tl, board)
        #self.find_right_num(tl_p, self.tl, board)
        
        try:
            self.find_right_num(tl_p, self.tl, board)
        except Exception as e:
            print e
            for d in self.tl:
                print d
            for l in board:
                print l
        
        
    def iter_func(self, tl_p, tl, board):
        """
        tl_p = self.find_right_num(tl_p, tl, board)
        next_dot_pos = self.find_next_dot(tlp, tl, board)
        if next_dot_pos != -1:
            self.iter_func(next_dot_pos, tl, board)
        """
        pass
        
    def find_next_dot(self, tl_p, tl, board):
        # handle the initial situation.
        if not tl:
            r = c = 0
        else:
            if tl_p != len(tl) - 1:
                return tl_p + 1
            else:
                r = tl[tl_p]['cur_r']
                c = tl[tl_p]['cur_c']
        while r < 9:
            while c < 9:
                if board[r][c] == '.':
                    tl.append(dict(cur_r=r, cur_c=c, is_passed=0, tried=list()))
                    #print tl
                    return tl_p + 1
                else:
                    c += 1
            else:
                c = 0
                r += 1
        else:
            # can not find the next dot, which means we have generate the answer.
            return -1
    
    def find_right_num(self, tl_p, tl, board):
        """
        try:
            cur_r = tl[tl_p]['cur_r']
            cur_c = tl[tl_p]['cur_c']
        except:
            cur_r = tl[0]['cur_r']
            cur_c = tl[0]['cur_c']
            tl_p = 0
        """
        #print tl_p
        cur_r = tl[tl_p]['cur_r']
        cur_c = tl[tl_p]['cur_c']
        existed_num = []
        # add the row.
        for e in board[cur_r]:
            if e != '.' and e not in existed_num:
                existed_num.append(e)
        #print existed_num
        # add the column.
        i = 0
        while i < 9:
            if board[i][cur_c] != '.' and board[i][cur_c] not in existed_num:
                existed_num.append(board[i][cur_c])
            i += 1
        #print existed_num
        # add the block.
        b_r = cur_r / 3
        b_c = cur_c / 3
        i = j = 0
        while i < 3:
            while j < 3:
                if board[b_r*3+i][b_c*3+j] != '.' and board[b_r*3+i][b_c*3+j] not in existed_num:
                    existed_num.append(board[b_r*3+i][b_c*3+j])
                j += 1
            j = 0
            i += 1
        #print existed_num
        # add the tried nums.
        for e in tl[tl_p]['tried']:
            if e not in existed_num:
                existed_num.append(e)
        try_val = 1
        while try_val <= 9:
            try_val = str(try_val)
            if try_val not in existed_num:
                # finds it.
                board[cur_r][cur_c] = try_val
                tl[tl_p]['is_passed'] = 1
                tl[tl_p]['tried'].append(try_val)
                #print 'changed: ', board[cur_r][cur_c]
                #print tl
                # find the next dot.
                """
                if tl_p == len(tl) - 1:
                    return self.find_next_dot(tl_p, tl, board)
                else:
                    return tl_p + 1
                """
                #return tl_p
                next_dot = self.find_next_dot(tl_p, tl, board)
                if next_dot == -1:
                    return
                else:
                    self.find_right_num(next_dot, tl, board)
            try_val = int(try_val)
            try_val += 1
        else:
            # can not find the right number to replace the dot.
            tl[tl_p]['is_passed'] = 0
            tl[tl_p]['tried'] = []
            board[cur_r][cur_c] = '.'
            last_r = tl[tl_p-1]['cur_r']
            last_c = tl[tl_p-1]['cur_c']
            board[cur_r][cur_c] = '.'
            tl[tl_p-1]['is_passed'] = 0
            #return tl_p-1
            self.find_right_num(tl_p-1, tl, board)
            
        
    
        
            