import java.rmi.*;
import java.rmi.registry.*;

public class Serveur {
    public static void main(String[] args) throws Exception {
        // Création de l'objet distant.
        Calculatrice objet = new CalculatriceImpl();

        // Démarrage du registre RMI sur le port par défaut.
        LocateRegistry.createRegistry(1099);

        // Publication de l'objet sous le nom Calculatrice.
        Naming.bind("rmi://localhost/Calculatrice", objet);
        System.out.println("Serveur prêt");
    }
}
