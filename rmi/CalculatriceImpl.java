import java.rmi.*;
import java.rmi.server.*;

// Implémentation de l'interface distante.
public class CalculatriceImpl extends UnicastRemoteObject implements Calculatrice {

    // Le constructeur exporte l'objet pour qu'il soit accessible à distance.
    public CalculatriceImpl() throws RemoteException {
        super();
    }

    @Override
    public double additionner(double a, double b) throws RemoteException {
        return a + b;
    }

    @Override
    public double multiplier(double a, double b) throws RemoteException {
        return a * b;
    }
}
