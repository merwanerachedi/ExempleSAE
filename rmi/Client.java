import java.rmi.*;

public class Client {
    public static void main(String[] args) throws Exception {
        // Recherche de l'objet publié par le serveur.
        Calculatrice calculatrice =
                (Calculatrice) Naming.lookup("rmi://localhost/Calculatrice");

        // Appels des méthodes distantes.
        System.out.println("10 + 5 = " + calculatrice.additionner(10, 5));
        System.out.println("10 x 5 = " + calculatrice.multiplier(10, 5));
    }
}
