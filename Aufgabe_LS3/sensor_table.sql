SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `sensor_data`;
CREATE TABLE `sensor_data` (
  `alpha` int(11) NOT NULL,
  `beta` int(11) NOT NULL,
  `gamma` int(11) NOT NULL,
  `index` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `date` timestamp NOT NULL,
  PRIMARY KEY (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;