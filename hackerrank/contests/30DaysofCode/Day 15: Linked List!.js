// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-15-linked-list

this.insert=function(head,data){
    if (head) {
        var tail = head;
        while (tail.next) {
            tail = tail.next;
        }
        var node = new Node(data);
        tail.next = node;
        return head;
    }
    
    var node = new Node(data);
    return node;
};
