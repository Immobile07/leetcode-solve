# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def ln(self,ll):
        cnt=0
        tmp=ll
        while(tmp!=None):
            cnt+=1
            tmp=tmp.next
        return cnt
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if self.ln(l1)==self.ln(l2):
            tmp1=l1
            tmp2=l2
            cr=0
            prev=None
            while(tmp1!=None and tmp2!=None):
                ad=tmp1.val + tmp2.val+cr
                cr=0
                if ad>=10:
                    ad=ad%10
                    cr=1
                    tmp1.val=ad
                    prev=tmp1
                    tmp1=tmp1.next
                    tmp2=tmp2.next
                else:
                    prev=tmp1
                    tmp1.val=ad
                    tmp1=tmp1.next
                    tmp2=tmp2.next
            if cr==0:

                return l1
            else:
                nw=ListNode(cr)
                prev.next=nw
                return l1
        elif self.ln(l1)>self.ln(l2):
            tmp1=l1
            tmp2=l2
            cr=0
            prev=None
            while(tmp1!=None and tmp2!=None):
                ad=tmp1.val + tmp2.val+cr
                if ad>=10:
                    ad=ad%10
                    cr=1
                    tmp1.val=ad
                    tmp1=tmp1.next
                    tmp2=tmp2.next
                else:
                    cr=0
                    tmp1.val=ad
                    tmp1=tmp1.next
                    tmp2=tmp2.next
            while(tmp1!=None):
                ad=tmp1.val+cr
                if ad>=10:
                    ad=ad%10
                    cr=1
                    tmp1.val=ad
                    prev=tmp1
                    tmp1=tmp1.next
                else:
                    cr=0
                    tmp1.val=ad
                    prev=tmp1
                    tmp1=tmp1.next
            if cr==0:

                return l1
            else:
                nw=ListNode(cr)
                prev.next=nw
                return l1
        else:
            tmp1=l1
            tmp2=l2
            cr=0
            prev=None
            while(tmp1!=None and tmp2!=None):
                ad=tmp1.val + tmp2.val+cr
                if ad>=10:
                    ad=ad%10
                    cr=1
                    tmp2.val=ad
                    tmp1=tmp1.next
                    tmp2=tmp2.next
                else:
                    cr=0
                    tmp2.val=ad
                    tmp1=tmp1.next
                    tmp2=tmp2.next
            while(tmp2!=None):
                ad=tmp2.val+cr
                if ad>=10:
                    ad=ad%10
                    cr=1
                    tmp2.val=ad
                    prev=tmp2
                    tmp2=tmp2.next
                else:
                    cr=0
                    tmp2.val=ad
                    prev=tmp2
                    tmp2=tmp2.next

            if cr==0:

                return l2
            else:
                nw=ListNode(cr)
                prev.next=nw
                return l2
            