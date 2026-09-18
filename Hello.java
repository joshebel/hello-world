public class Hello {
    /**
     * Hello World with INTENTIONAL vulnerabilities for code-scanner testing.
     *
     * CWE-78: OS command injection via Runtime.exec()
     * CWE-89: SQL injection via string-concatenated query
     *
     * Do not use these patterns in real software.
     */
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");

        if (args.length == 0) {
            System.out.println("Usage: java Hello <name>");
            return;
        }

        String name = args[0];

        // INTENTIONAL command injection: unsanitized user input passed to the shell.
        Runtime.getRuntime().exec("/bin/sh -c echo Hello, " + name);

        // INTENTIONAL SQL injection: unsanitized user input concatenated into a query.
        String query = "SELECT * FROM users WHERE name = '" + name + "'";
        System.out.println("Would execute: " + query);
    }
}
