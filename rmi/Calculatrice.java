import java.rmi.*;

public interface Calculatrice extends Remote {
    double additionner(double a, double b) throws RemoteException;

    double multiplier(double a, double b) throws RemoteException;
}
