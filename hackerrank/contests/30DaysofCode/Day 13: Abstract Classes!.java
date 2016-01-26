// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-13-abstract-classes

class MyBook extends Book {
    private int price;
    public MyBook (String title, String author, int price) {
        super(title, author);
        this.price = price;
    }
    
    void display() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Price: " + this.price);
    }
}
