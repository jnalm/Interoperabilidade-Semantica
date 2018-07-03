DROP TRIGGER novoPedido;

DELIMITER //
CREATE TRIGGER novoPedido
AFTER INSERT ON Pedido
FOR EACH ROW
	BEGIN
    
        INSERT INTO Worklist VALUES (null, NEW.idPedido);
		
  END; //
  DELIMITER ;
  SELECT COUNT(*) FROM Worklist
  SELECT * FROM Worklist
  SELECT * FROM Pedido
DELETE FROM Worklist WHERE idWorklist > 0;
DELETE FROM Pedido WHERE idPedido > 0;
INSERT INTO Pedido (idPedido, descricao, hora, data, idEpisode, idDoente) VALUES (1, 'cardiologia', '34567', '56789', NULL, 1);
INSERT INTO Pedido VALUES (2, 'cardiologia', '34567', '56789', NULL, 1);
INSERT INTO Doente VALUES (1, 1, 'tu', 'ola');