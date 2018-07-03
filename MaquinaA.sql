-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema is
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema is
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `is` DEFAULT CHARACTER SET utf8 ;
USE `is` ;

-- -----------------------------------------------------
-- Table `is`.`Episode`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `is`.`Episode` (
  `idEpisode` INT NOT NULL,
  `tipo` VARCHAR(45) NULL,
  PRIMARY KEY (`idEpisode`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `is`.`Doente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `is`.`Doente` (
  `idDoente` INT NOT NULL AUTO_INCREMENT,
  `idProcesso` INT NULL,
  `morada` VARCHAR(45) NULL,
  `telefone` VARCHAR(45) NULL,
  `nome` VARCHAR(45) NULL,
  `sexo` VARCHAR(45) NULL,
  PRIMARY KEY (`idDoente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `is`.`Pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `is`.`Pedido` (
  `idPedido` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(45) NULL,
  `hora` VARCHAR(45) NULL,
  `data` VARCHAR(45) NULL,
  `idEpisode` INT NULL,
  `idDoente` INT NOT NULL,
  `relatorio` VARCHAR(10000) NULL,
  `estado` VARCHAR(45) NULL,
  `medico` VARCHAR(45) NULL,
  `tipo` VARCHAR(45) NULL,
  PRIMARY KEY (`idPedido`, `idDoente`),
  INDEX `fk_Pedido_Episode1_idx` (`idEpisode` ASC),
  INDEX `fk_Pedido_Doente1_idx` (`idDoente` ASC),
  CONSTRAINT `fk_Pedido_Episode1`
    FOREIGN KEY (`idEpisode`)
    REFERENCES `is`.`Episode` (`idEpisode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pedido_Doente1`
    FOREIGN KEY (`idDoente`)
    REFERENCES `is`.`Doente` (`idDoente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `is`.`Worklist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `is`.`Worklist` (
  `idWorklist` INT NOT NULL AUTO_INCREMENT,
  `idPedido` INT NOT NULL,
  `relatorio` VARCHAR(10000) NULL,
  PRIMARY KEY (`idWorklist`, `idPedido`),
  INDEX `fk_Worklist_Pedido1_idx` (`idPedido` ASC),
  CONSTRAINT `fk_Worklist_Pedido1`
    FOREIGN KEY (`idPedido`)
    REFERENCES `is`.`Pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
