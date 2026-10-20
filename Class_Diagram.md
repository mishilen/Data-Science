- ## Class Diagram
	- Class diagrams model software at a high level without source code.
	- They show class names, attributes, methods, and relationships but not its functionality.
	- They map directly to source code classes.
	- ## UML (Unified Modeling Language)
		- ensures diagrams are universally readable and standardized.
		- Class → Represented as a rectangle with three sections: class name, attributes, and methods.
			* Attributes → Written as `name:type`. Use `+` for public, `-` for private.
			* Constructors listed in methods section, written as `+ClassName(paramName:type)`.
			* Methods Written as `+methodName(param:type):returnType`.

			-
			  ```code0
			  public class Person {
			      private String name;
			      private int age;
			      public Person(String initialName) {
			          this.name = initialName;
			          this.age = 0;
			      }
			      public void printPerson() {
			          System.out.println(this.name + ", age " +   this.age + " years");
			      }
			      public String getName() {
			          return this.name;
			      }
			  }
			  ```
			-
			  | Person |
			  |---|
			  | _ |
			  | -name:String |
			  | -age:int |
			  | _ |
			  | +Person(initialName:String) |
			  | +printPerson():void |
			  | +getName():String |
		- Instance variables that refer to another object are not listed as attributes. Instead, they are shown as arrows between classes.
			* The arrow direction shows who knows whom (e.g., `Book → Person` means a `Book` knows its `Person` author).
			* Arrows can have labels like “author” or “authors.”
			* Labels can be added to the arrow (e.g., “author” or “authors”) for clarity.

			-
			  ```code
			  [Person|-name:String;-age:int]  
			  [Book|-name:String;-publisher:String]  
			  [Book] -*-> [Person]   // Book can have many Persons as authors
			  ```
		- If there is no arrowhead in a connection, both classes know about each other.