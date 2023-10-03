// Lab Sheet 1.1: Create a java program using Single Inheritance.

class Animal {
    void eat() {
        System.out.println("The animal eats food.");
    }
}
// Subclass inheriting from Animal
class Dog extends Animal {
    void bark() {
        System.out.println("The dog barks.");
    }
}
public class Main {
    public static void main(String[] args) {
        // Create an instance of the Dog class
        Dog myDog = new Dog();
        // Call methods from both the superclass and subclass
        myDog.eat(); // Inherited from Animal
        myDog.bark(); // Defined in Dog
    }
}

// Lab Sheet 1.2: Create a java program using Multilevel Inheritance.
// The base class
class Animal {
    void eat() {
        System.out.println("Animal is eating");
    }
}
// Subclass 1: Mammal, inherits from Animal
class Mammal extends Animal {
    void run() {
        System.out.println("Mammal is running");
    }
}

// Subclass 2: Dog, inherits from Mammal
class Dog extends Mammal {
    void bark() {
        System.out.println("Dog is barking");
    }
}
public class Main {
    public static void main(String[] args) {
        // Create an instance of Dog
        Dog myDog = new Dog();
        // Call methods from each class in the hierarchy
        myDog.eat();   // Inherited from Animal
        myDog.run();   // Inherited from Mammal
        myDog.bark();  // Defined in Dog
    }

// Lab Sheet 2: Create a java program using constructor with keyword ‘super’.
class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

class Employee extends Person {
    private String employeeId;

    public Employee(String name, int age, String employeeId) {
        super(name, age);
        this.employeeId = employeeId;
    }

    public void displayEmployeeInfo() {
        super.displayInfo();
        System.out.println("Employee ID: " + employeeId);
    }
}

class Student extends Person {
    private String studentId;

    public Student(String name, int age, String studentId) {
        super(name, age);
        this.studentId = studentId;
    }

    public void displayStudentInfo() {
        super.displayInfo();
        System.out.println("Student ID: " + studentId);
    }
}

public class MultiLevelInheritanceExample {
    public static void main(String[] args) {
        Employee employee = new Employee("John", 30, "EMP12345");
        Student student = new Student("Alice", 20, "STU67890");

        System.out.println("Employee Information:");
        employee.displayEmployeeInfo();

        System.out.println("\nStudent Information:");
        student.displayStudentInfo();
    }
}

// Lab Sheet3. Create a single thread by implementing Runnable interface.

import java.lang.*; //optional
class Task implements Runnable {    
    public void run() {
       System.out.println(Thread.currentThread()+" printing ");  
        System.out.println("Welcome");  
    }  
}
  public class TestThread { 
  public static void main(String[] args) {  
  Task task = new Task();
  Thread t1= new Thread(task);  
   t1.setName("first");
   t1.start();  
 System.out.println(Thread.currentThread()+" printing ");
 System.out.println("to Java");  
  }
}

//  Create a single thread by extending Thread class

class MyThread extends Thread {  
    // run() method to perform action for thread.   
    public void run()  
    {    
       int a= 10;  
       int b=12;  
       int result = a+b;  
       System.out.println(Thread.currentThread()+" started running..");  
       System.out.println("Sum of two numbers is: "+ result);  
      System.out.println(Thread.currentThread()+" completed..");  
    }  
}
public class TestThread {
    public static void main( String args[] )  
    {  
    System.out.println(Thread.currentThread()+" started");
     // Creating instance of the class extend Thread class  
       MyThread t = new  MyThread();  
       t.setName("first");
       //calling start method to execute the run() method of the Thread class  
       t.start();  
    System.out.println(Thread.currentThread()+" completed");
    }  
}

// Lab Sheet 4.1 Create a single thread by extending Thread class

class MyThread extends Thread {  
    // run() method to perform action for thread.   
    public void run()  
    {    
       int a= 10;  
       int b=12;  
       int result = a+b;  
       System.out.println(Thread.currentThread()+" started running..");  
       System.out.println("Sum of two numbers is: "+ result);  
      System.out.println(Thread.currentThread()+" completed..");  
    }  
}
public class TestThread {
    public static void main( String args[] )  
    {  
    System.out.println(Thread.currentThread()+" started");
     // Creating instance of the class extend Thread class  
       MyThread t = new  MyThread();  
       t.setName("first");
       //calling start method to execute the run() method of the Thread class  
       t.start();  
    System.out.println(Thread.currentThread()+" completed");
    }  
}

// Lab Sheet 4.2: Create 3 threads 1st, 2nd and 3rd to print numbers 5 to 1 concurrently by extending Thread Class. 
// Requirement:
// •Override run() to print 5 to 1 using for loop 
// •Use sleep() for switching the context to other threads
// •Use setName() to set the name of Thread or Use constructor Thread() to set the name of Thread

class MyThread extends Thread {  
    String name;
            MyThread (String name){  
                       setName(name);   or //  super(name);
                       this.name=name;
                System.out.println( "A New thread: " + name + "is created\n" );          
        }  
        public void run() {  
        try {  
            for(int j = 5; j > 0; j--) {  
                System.out.println(name + ": " + j);  
                Thread.sleep(1000);  
            }  
        }catch (InterruptedException e) {  
            System.out.println(name + " thread Interrupted");  
        }  
         System.out.println(name + " thread exiting.");  
        }  
    }  
    public class TestMultiThread {    
        public static void main(String args[]) {  
            MyThread t1=new MyThread(“one”);  
            MyThread t2=new MyThread(“two”);  
            MyThread t3=new MyThread(“three”);  
            t1.start();
            t2.start();
            t3.start();   
            try {  
                Thread.sleep(8000);  
            } catch (InterruptedException excetion) {  
                System.out.println("Inturruption occurs in Main Thread");  
            }  
            System.out.println("We are exiting from Main Thread");  
        }  

// Lab Sheet 4.3:Create 3 threads 1st, 2nd and 3rd to print factorial of three different numbers concurrently by extending Thread Class. 
// Requirement:
// •Override run() to print factorial using for loop 
// •Use sleep() for switching the context to other threads
// •Use constructor Thread() to set the name of Thread
// •Demonstrate join() and isAlive() method

class MyThread extends Thread {  
    String name;
    int number;
    long fact=1;
            MyThread (int number,String name){  
                   super(name);    //calling Thread()
                   this.number=number;
                   this.name=name;
                  System.out.println( "A New thread: " + name + " is created\n" );          
        }  
        public void run() {  
        try {  
            for(int i = 1; i <= number; i++) {  
                System.out.println(name + " calculating factorial"); 
                fact=fact*i; 
                Thread.sleep(1000);  
            }  
          
        }catch (InterruptedException e) {  
            System.out.println(name + " thread Interrupted");  
        }  
         System.out.println(name + " calculated factorial "+fact);   
        }  }  
    public class TestMultiThread {    
        public static void main(String args[]) {  
            MyThread t1=new MyThread(5,"one");  
            MyThread t2=new MyThread(4,"two");  
            MyThread t=new MyThread(3,"three");  
            t1.start();
            t2.start();
            t3.start();   
         System.out.println("1st Alive : "+t1.isAlive());
         System.out.println("2nd Alive : "+t2.isAlive());
         System.out.println("3rd Alive : "+t3.isAlive());
            try {  
              t1.join();
               t2.join();
               t3.join();
    System.out.println("1st Alive : "+t1.isAlive());
    System.out.println("2nd Alive : "+t2.isAlive());
    System.out.println("3rd Alive : "+t3.isAlive());         
    } catch (InterruptedException excetion) {  
                System.out.println("Inturruption occurs in Main Thread");  
            }  
            System.out.println("We are exiting from Main Thread");  
        }  
    }

// Lab Sheet 5.1: Create three threads by setting different priorities to each thread.

class ThreadPrior extends Thread {
 
    public void run()
    {
        // Print statement
        System.out.println("Inside run method");
    }
 
}
public class TestThreadPrior {
    public static void main(String[] args)
    {
        ThreadPrior t1 = new ThreadPrior();
        ThreadPrior t2 = new ThreadPrior();
        ThreadPrior t3 = new ThreadPrior();
 
        System.out.println("t1 thread priority : "+ t1.getPriority());
        System.out.println("t2 thread priority : "+ t2.getPriority());
        System.out.println("t3 thread priority : "+ t3.getPriority());
         
        t1.setPriority(2);
        t2.setPriority(5);
        t3.setPriority(8);
 
        t3.setPriority(21); //error
        System.out.println("t1 thread priority : " + t1.getPriority());
        System.out.println("t2 thread priority : "+ t2.getPriority());
       
        System.out.println("t3 thread priority : " + t3.getPriority());
 
        // Main thread
 
        System.out.println("Currently Executing Thread : "+Thread.currentThread().getName());
 
        System.out.println(
            "Main thread priority : "+ Thread.currentThread().getPriority());
 
        // Main thread priority is set to 10
        Thread.currentThread().setPriority(10);
 
        System.out.println(
            "Main thread priority : "+ Thread.currentThread().getPriority());
    }
}

// Lab Sheet 5.2: Demonstrate Thread Synchronization for a given resource to avoid race condition.
// •Create a Resource class to keep two resources [ and ]. No thread can take ] without [
// •Create three threads to access the above resource without synchronization
// •Access the above resource using synchronization  
     
    class Resource {
         void use(String name) {
         System.out.print("[" + name);
         try {
          Thread.sleep(1000);
       } catch(InterruptedException e) {
            System.out.println("Interrupted");
          }
         System.out.println("]");
         }
    }
    
    class MyThread extends Thread {  
           String name;
           Resource r;
            MyThread (String name,Resource r){ 
            super(name);
            this.name = name;   
            this.r=r;
        }  
        public void run() {  
            synchronized(r) {
            r.use(name); 
           }
        }  
    }  
    public class TestMultiThread {    
        public static void main(String args[]) {  
            Resource res=new Resource();
            MyThread t1=new MyThread("1st",res);  
            MyThread t2=new MyThread("2nd",res);  
            MyThread t3=new MyThread("3rd",res);  
            t1.start();
            t2.start();
            t3.start();   
            try {  
                t1.join(); 
                t2.join(); 
                t3.join(); 
            } catch (InterruptedException excetion) {  
                System.out.println("Inturruption occurs in Main Thread");  
            }  
            }  
    }                        
