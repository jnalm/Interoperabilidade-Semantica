DELIMITER //
CREATE TRIGGER novoPedido
AFTER INSERT ON Pedido
FOR EACH ROW
	BEGIN
    
        INSERT INTO Worklist VALUES (null, NEW.idPedido, null);
		
  END; //
  DELIMITER ;
  
DELIMITER //
CREATE TRIGGER updatePedido
AFTER UPDATE ON Pedido
FOR EACH ROW
	BEGIN
    
        INSERT INTO Worklist VALUES (null, NEW.idPedido, NEW.relatorio);
		
  END; //
  DELIMITER ;