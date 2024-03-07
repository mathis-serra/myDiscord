-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: discord
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `channels`
--

DROP TABLE IF EXISTS `channels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `channels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channels`
--

LOCK TABLES `channels` WRITE;
/*!40000 ALTER TABLE `channels` DISABLE KEYS */;
INSERT INTO `channels` VALUES (1,'Sfi Community','2024-03-07 10:57:24'),(2,'MMKWW','2024-03-07 10:58:48'),(3,'Reading Rooms','2024-03-07 10:59:12');
/*!40000 ALTER TABLE `channels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `channel_id` int NOT NULL,
  `content` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL,
  `modified_at` timestamp NOT NULL,
  `user_friend` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (6,19,0,'aa à 14:25 \nsdfsdf','2024-03-05 13:25:24','2024-03-05 13:25:24',21),(7,19,0,'aa à 14:26 \nsfsdf','2024-03-05 13:26:12','2024-03-05 13:26:12',21),(8,19,0,'aa à 14:26 \ngkg','2024-03-05 13:26:13','2024-03-05 13:26:13',21),(9,19,0,'aa à 14:26 \nlf','2024-03-05 13:26:17','2024-03-05 13:26:17',21),(10,19,0,'aa à 14:26 \nmaximeee','2024-03-05 13:26:59','2024-03-05 13:26:59',21),(11,19,0,'aa à 13:37 \niuuu','2024-03-06 12:37:08','2024-03-06 12:37:08',21),(12,19,0,'aa à 13:37 \nyui','2024-03-06 12:37:11','2024-03-06 12:37:11',21),(13,19,0,'aa à 13:40 \njkrt','2024-03-06 12:40:13','2024-03-06 12:40:13',21),(14,19,0,'aa à 13:40 \nrykje','2024-03-06 12:40:14','2024-03-06 12:40:14',21),(15,19,0,'aa à 13:44 \njkj','2024-03-06 12:44:44','2024-03-06 12:44:44',21),(16,19,0,'aa à 14:02 \ndskfj','2024-03-06 13:02:49','2024-03-06 13:02:49',21),(17,19,0,'aa à 14:02 \ndsf','2024-03-06 13:02:54','2024-03-06 13:02:54',21),(18,19,0,'aa à 14:02 \ndsf','2024-03-06 13:02:54','2024-03-06 13:02:54',21),(19,19,0,'aa à 14:03 \ndsf','2024-03-06 13:03:05','2024-03-06 13:03:05',21),(20,19,0,'aa à 14:03 \ndsfgsdg','2024-03-06 13:03:15','2024-03-06 13:03:15',21),(21,19,0,'aa à 14:03 \nsdg','2024-03-06 13:03:16','2024-03-06 13:03:16',21),(22,19,0,'aa à 14:03 \ndfg','2024-03-06 13:03:17','2024-03-06 13:03:17',21),(23,19,0,'aa à 14:03 \ndfgdfg','2024-03-06 13:03:18','2024-03-06 13:03:18',21),(24,19,0,'aa à 14:04 \ndg','2024-03-06 13:04:43','2024-03-06 13:04:43',21),(25,19,0,'aa à 14:04 \nsdfsdf','2024-03-06 13:04:47','2024-03-06 13:04:47',21),(26,19,0,'aa à 14:05 \nskdgj','2024-03-06 13:05:37','2024-03-06 13:05:37',21),(27,19,0,'aa à 14:07 \nsdf','2024-03-06 13:07:56','2024-03-06 13:07:56',20),(28,19,0,'aa à 14:07 \nfgddfg','2024-03-06 13:07:57','2024-03-06 13:07:57',20),(29,19,0,'aa à 14:07 \nfdh','2024-03-06 13:07:57','2024-03-06 13:07:57',20),(30,19,0,'aa à 14:07 \nfgh','2024-03-06 13:07:58','2024-03-06 13:07:58',20),(31,19,0,'aa à 14:07 \ngfh','2024-03-06 13:07:58','2024-03-06 13:07:58',20),(32,19,0,'aa à 14:07 \ngfh','2024-03-06 13:07:59','2024-03-06 13:07:59',20),(33,19,0,'aa à 14:07 \ngfj','2024-03-06 13:07:59','2024-03-06 13:07:59',20),(34,19,0,'aa à 14:07 \nghj','2024-03-06 13:07:59','2024-03-06 13:07:59',20),(35,19,0,'aa à 14:07 \nhgj','2024-03-06 13:08:00','2024-03-06 13:08:00',20),(36,19,0,'aa à 14:08 \ndfg','2024-03-06 13:08:00','2024-03-06 13:08:00',20),(37,19,0,'aa à 14:08 \ndg','2024-03-06 13:08:01','2024-03-06 13:08:01',20),(38,19,0,'aa à 14:08 \ngfj','2024-03-06 13:08:01','2024-03-06 13:08:01',20),(39,19,0,'aa à 14:08 \nghj','2024-03-06 13:08:01','2024-03-06 13:08:01',20),(40,19,0,'aa à 14:08 \ndg','2024-03-06 13:08:02','2024-03-06 13:08:02',20),(41,19,0,'aa à 14:08 \nsdf','2024-03-06 13:08:02','2024-03-06 13:08:02',20),(42,19,0,'aa à 14:08 \nsqf','2024-03-06 13:08:03','2024-03-06 13:08:03',20),(43,19,0,'aa à 14:08 \ndsg','2024-03-06 13:08:03','2024-03-06 13:08:03',20),(44,19,0,'aa à 14:08 \ndsg','2024-03-06 13:08:03','2024-03-06 13:08:03',20),(45,19,0,'aa à 14:10 \nsdlfk','2024-03-06 13:10:15','2024-03-06 13:10:15',21),(46,19,0,'aa à 14:10 \nsdkgjdfg','2024-03-06 13:10:16','2024-03-06 13:10:16',21),(47,19,0,'aa à 14:10 \nsqdlk','2024-03-06 13:10:17','2024-03-06 13:10:17',21),(48,19,0,'aa à 14:10 \ndskj','2024-03-06 13:10:39','2024-03-06 13:10:39',11),(49,19,0,'aa à 14:10 \ndfgkj','2024-03-06 13:10:40','2024-03-06 13:10:40',11),(50,19,0,'aa à 14:10 \nfdgkj','2024-03-06 13:10:40','2024-03-06 13:10:40',11),(51,19,0,'aa à 14:10 \ndfgkjdf','2024-03-06 13:10:41','2024-03-06 13:10:41',11),(52,19,0,'aa à 14:10 \ndfg','2024-03-06 13:10:41','2024-03-06 13:10:41',11),(53,19,0,'aa à 14:10 \ndfg','2024-03-06 13:10:42','2024-03-06 13:10:42',11),(54,19,0,'aa à 14:10 \ndfg','2024-03-06 13:10:42','2024-03-06 13:10:42',11),(55,19,0,'aa à 14:10 \ndfg','2024-03-06 13:10:42','2024-03-06 13:10:42',11),(56,19,0,'aa à 14:10 \ndfg','2024-03-06 13:10:43','2024-03-06 13:10:43',11),(57,19,0,'aa à 14:10 \ndfg','2024-03-06 13:10:43','2024-03-06 13:10:43',11),(58,19,0,'aa à 14:10 \ndfg','2024-03-06 13:10:44','2024-03-06 13:10:44',11),(59,19,0,'aa à 14:10 \ndfg','2024-03-06 13:10:44','2024-03-06 13:10:44',11),(60,19,0,'aa à 14:10 \ndfg','2024-03-06 13:10:44','2024-03-06 13:10:44',11),(61,19,0,'aa à 14:10 \ngj','2024-03-06 13:10:45','2024-03-06 13:10:45',11),(62,19,0,'aa à 14:10 \nghjghj','2024-03-06 13:10:45','2024-03-06 13:10:45',11),(63,19,0,'aa à 14:10 \nk','2024-03-06 13:10:45','2024-03-06 13:10:45',11),(64,19,0,'aa à 14:10 \n','2024-03-06 13:10:46','2024-03-06 13:10:46',11),(65,19,0,'aa à 14:18 \nsdg','2024-03-06 13:18:01','2024-03-06 13:18:01',21),(66,19,0,'aa à 14:18 \nfdg','2024-03-06 13:18:02','2024-03-06 13:18:02',21),(67,19,0,'aa à 14:18 \ndsfl,','2024-03-06 13:18:07','2024-03-06 13:18:07',21),(68,19,0,'aa à 14:18 \nsdf','2024-03-06 13:18:08','2024-03-06 13:18:08',21),(69,19,0,'aa à 14:18 \ndfhfg','2024-03-06 13:18:10','2024-03-06 13:18:10',21),(70,19,0,'aa à 14:18 \n','2024-03-06 13:18:11','2024-03-06 13:18:11',21),(71,19,0,'aa à 14:18 \ngfh','2024-03-06 13:18:12','2024-03-06 13:18:12',21),(72,19,0,'aa à 14:18 \nsdf','2024-03-06 13:18:56','2024-03-06 13:18:56',10),(73,19,0,'aa à 14:18 \ndsf','2024-03-06 13:18:56','2024-03-06 13:18:56',10),(74,19,0,'aa à 14:18 \ndsf','2024-03-06 13:18:57','2024-03-06 13:18:57',10),(75,19,0,'aa à 14:18 \ndsf','2024-03-06 13:18:57','2024-03-06 13:18:57',10),(76,19,0,'aa à 14:18 \nsdf','2024-03-06 13:18:58','2024-03-06 13:18:58',10),(77,19,0,'aa à 14:18 \nsdf','2024-03-06 13:18:58','2024-03-06 13:18:58',10),(78,19,0,'aa à 14:18 \ndsf','2024-03-06 13:18:59','2024-03-06 13:18:59',10),(79,19,0,'aa à 14:18 \nsdf','2024-03-06 13:18:59','2024-03-06 13:18:59',10),(80,19,0,'aa à 14:41 \nsqd','2024-03-06 13:41:10','2024-03-06 13:41:10',10),(81,19,0,'aa à 14:41 \nqsdf','2024-03-06 13:41:30','2024-03-06 13:41:30',18),(82,19,0,'aa à 14:51 \nqsfqsf','2024-03-06 13:51:21','2024-03-06 13:51:21',23),(83,19,0,'aa à 14:51 \nsdfsdf','2024-03-06 13:51:22','2024-03-06 13:51:22',23),(84,19,0,'aa à 14:58 \nqfksldf','2024-03-06 13:58:24','2024-03-06 13:58:24',18),(85,19,0,'aa à 16:28 \nsdlkqsd','2024-03-06 15:28:17','2024-03-06 15:28:17',18),(86,19,0,'aa à 11:59 \ndosq','2024-03-07 10:59:31','2024-03-07 10:59:31',3),(87,19,0,'aa à 11:59 \nkjg','2024-03-07 10:59:34','2024-03-07 10:59:34',3);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servers`
--

DROP TABLE IF EXISTS `servers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `owner_id` int NOT NULL,
  `roles` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servers`
--

LOCK TABLES `servers` WRITE;
/*!40000 ALTER TABLE `servers` DISABLE KEYS */;
/*!40000 ALTER TABLE `servers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_channel`
--

DROP TABLE IF EXISTS `user_channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_channel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` bigint DEFAULT NULL,
  `channel_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `channel_id` (`channel_id`),
  CONSTRAINT `user_channel_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `user_channel_ibfk_2` FOREIGN KEY (`channel_id`) REFERENCES `channels` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_channel`
--

LOCK TABLES `user_channel` WRITE;
/*!40000 ALTER TABLE `user_channel` DISABLE KEYS */;
INSERT INTO `user_channel` VALUES (1,19,1),(2,19,1),(3,19,1),(4,19,1);
/*!40000 ALTER TABLE `user_channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userroles`
--

DROP TABLE IF EXISTS `userroles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userroles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `role_id` int NOT NULL,
  `created_at` timestamp NOT NULL,
  `color` varchar(255) DEFAULT NULL,
  `permissions` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userroles`
--

LOCK TABLES `userroles` WRITE;
/*!40000 ALTER TABLE `userroles` DISABLE KEYS */;
/*!40000 ALTER TABLE `userroles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `role` int NOT NULL DEFAULT '1',
  `username` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (7,'z','z','z','z',1,'zz'),(8,'','','','',1,''),(9,'a','a','sqdsq','z',1,'aa'),(10,'zrer','asqd','zsd','z',1,'zreasq'),(11,'fjksdhfkjsdf','dds','sd','sd',1,'fjkdds'),(12,'b','aze','aze','aze',1,'baze'),(13,'1','2','3','4',1,'12'),(14,'3','4','1','2',1,'34'),(15,'3','4','7','7',1,'34'),(16,'sdf','dfs','8','sqf',1,'sdfdfs'),(17,'sdf','dfs','9','sqf',1,'sdfdfs'),(18,'qsd','sdd','blabla@laplateforme.io','qsd',1,'qsdsdd'),(19,'a','a','a@laplateforme.io','a',1,'aa'),(20,'a','a','oui@laplateforme.io','a',1,'aa'),(21,'myname','jeremy','lala@laplateforme.io','a',1,'mynjer'),(22,'myname','jeremy','la@laplateforme.io','a',1,'mynjer'),(23,'Jeremy','Boateng','laopqsod@laplateforme.io','a',1,'JerBoa'),(24,'Jeremy','Boateng','p@laplateforme.io','a',1,'JerBoa');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-07 14:16:11
