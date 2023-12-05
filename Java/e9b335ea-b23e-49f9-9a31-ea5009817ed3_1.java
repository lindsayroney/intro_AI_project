interface Animal {
    String sound();
}

class Dog implements Animal {
    public String sound() {
        return "Woof";
    }
}

class Main {
    public static void main(String[] args) {
        Animal animal = new Dog();
        System.out.println(animal.sound()); // Output: Woof
    }
}
