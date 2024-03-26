-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 26, 2024 at 07:18 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `habit_tracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `completed_habits`
--

CREATE TABLE `completed_habits` (
  `complete_id` varchar(15) NOT NULL,
  `user_id` varchar(8) DEFAULT NULL,
  `habit_id` varchar(15) DEFAULT NULL,
  `completion_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `completed_habits`
--

INSERT INTO `completed_habits` (`complete_id`, `user_id`, `habit_id`, `completion_date`) VALUES
('11648461507082', '77387001', '18742679683229', '2023-03-18'),
('12251999395899', '84615070', '16507919381095', '2020-07-04'),
('12951673295046', '52166444', '98275512898558', '2023-03-07'),
('16705856795081', '99899074', '38195439245203', '2023-03-19'),
('20008481509082', '40993249', '64895206698560', '2023-12-19'),
('21148481509082', '40993249', '64895206698560', '2023-12-18'),
('22878383928675', '40993249', '56297664251321', '2023-12-28'),
('23598074373606', '77387001', '18742679683229', '2023-03-02'),
('26851638312487', '40993249', '58961859285181', '2023-12-25'),
('27015719527272', '40993249', '69928045660556', '2023-12-20'),
('29123991767333', '84615070', '16507919381095', '2020-07-25'),
('29851991395676', '84615070', '16507919381095', '2020-07-24'),
('31696951174303', '52166444', '98275512898558', '2023-02-28'),
('33955646626040', '40993249', '16548615158461', '2023-12-29'),
('35472686614742', '77387001', '18742679683229', '2023-03-04'),
('40793024381195', '77751626', '64033732316412', '2024-03-19'),
('43570355196809', '77387001', '18742679683229', '2023-03-09'),
('48379916012137', '77387001', '90842994913069', '2023-11-30'),
('50563808246295', '52166444', '98275512898558', '2023-02-22'),
('51032053918111', '99899074', '38195439245203', '2023-03-15'),
('58094338401986', '40993249', '47312092427142', '2023-12-28'),
('58301557654236', '40993249', '56297664251321', '2023-12-25'),
('58680733913901', '40993249', '69574406644785', '2023-12-28'),
('58682448526231', '40993249', '58961859285181', '2023-12-28'),
('61038832493174', '77387001', '18742679683229', '2023-03-25'),
('63204034404893', '40993249', '16162818252063', '2023-12-28'),
('65658533575443', '40993249', '69928045660556', '2023-12-28'),
('70769001983805', '40993249', '64895206698560', '2023-12-20'),
('71101697895553', '52166444', '98275512898558', '2023-02-21'),
('74929534864762', '40993249', '47312092427142', '2023-12-21'),
('76551111444666', '84615070', '16507919381095', '2020-07-11'),
('76551121395777', '84615070', '16507919381095', '2020-07-08'),
('76551612395900', '84615070', '16507919381095', '2020-07-03'),
('77516863698013', '80593236', '59118012440636', '2024-01-12'),
('85446081699701', '40993249', '58961859285181', '2023-12-20'),
('86822972939735', '84615070', '27709554481051', '2024-03-12'),
('87283663358747', '52166444', '98275512898558', '2023-03-06'),
('87951321395490', '84615070', '16507919381095', '2020-07-17'),
('90251321395853', '84615070', '16507919381095', '2020-07-15'),
('90489143229974', '52166444', '98275512898558', '2023-03-13'),
('92440837213722', '40993249', '64895206698560', '2023-12-28'),
('92630868928734', '99899074', '38195439245203', '2023-03-17'),
('93508696470035', '99899074', '38195439245203', '2023-03-18'),
('94559581406321', '99899074', '38195439245203', '2023-03-13'),
('94670031385548', '40993249', '69928045660556', '2023-12-21'),
('96182761918242', '40993249', '11079963450879', '2023-12-28'),
('97028136978772', '77387001', '18742679683229', '2023-03-14'),
('97277389416042', '99899074', '38195439245203', '2023-03-22'),
('97546464969158', '40993249', '69574406644785', '2023-12-21'),
('97576834483974', '99899074', '38195439245203', '2023-03-21'),
('97678629011145', '77387001', '18742679683229', '2023-03-21'),
('98853332395435', '84615070', '16507919381095', '2020-07-10'),
('99048421107555', '84615070', '16507919381095', '2020-07-01');

-- --------------------------------------------------------

--
-- Table structure for table `habit`
--

CREATE TABLE `habit` (
  `habit_id` varchar(15) NOT NULL,
  `user_id` varchar(8) DEFAULT NULL,
  `task` varchar(256) DEFAULT NULL,
  `frequency` varchar(9) DEFAULT NULL,
  `period` varchar(100) DEFAULT NULL,
  `statuz` varchar(13) DEFAULT 'IN_PROGRESS',
  `start_date` date DEFAULT curdate(),
  `stop_date` date DEFAULT current_timestamp(),
  `ordering_time` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `habit`
--

INSERT INTO `habit` (`habit_id`, `user_id`, `task`, `frequency`, `period`, `statuz`, `start_date`, `stop_date`, `ordering_time`) VALUES
('11079963450879', '40993249', 'Do A', 'Daily', 'Everyday', 'IN_PROGRESS', '2023-12-21', '2023-12-21', '2023-12-21 02:42:39'),
('13416924176793', '52166444', 'Read a novel', 'Weekly', 'Wednesday Friday', 'IN_PROGRESS', '2023-11-23', '2023-12-13', '2023-12-21 02:40:00'),
('16162818252063', '40993249', 'Do some yogo', 'Weekly', 'Friday Wednesday Thursday', 'IN_PROGRESS', '2023-12-21', '2023-12-21', '2023-12-21 02:40:00'),
('16507919381095', '84615070', 'Study Chess', 'Weekly', 'Wednesday Friday Saturday', 'STOPPED', '2020-07-01', '2020-07-26', '2020-07-01 02:42:39'),
('16548615158461', '40993249', 'Do another press up', 'Weekly', 'Friday Tuesday', 'IN_PROGRESS', '2023-12-21', '2023-12-21', '2023-12-21 02:40:00'),
('18742679683229', '77387001', 'Jogging Early Mornings', 'Weekly', 'Monday Wednesday Saturday', 'STOPPED', '2020-03-01', '2023-03-25', '2023-12-21 02:40:00'),
('27709554481051', '84615070', 'gym', 'Daily', 'Everyday', 'IN_PROGRESS', '2024-03-12', '2024-03-12', '2024-03-12 15:39:07'),
('38195439245203', '99899074', 'Exercise', 'Daily', 'Everyday', 'STOPPED', '2020-03-13', '2023-03-22', '2023-12-21 02:40:00'),
('47312092427142', '40993249', 'Do B', 'Weekly', 'Saturday Monday Thursday', 'IN_PROGRESS', '2023-12-21', '2023-12-21', '2023-12-21 02:44:13'),
('56297664251321', '40993249', 'do some press up', 'Daily', 'Everyday', 'IN_PROGRESS', '2023-12-21', '2023-12-21', '2023-12-21 02:40:00'),
('58961859285181', '40993249', 'read python', 'Daily', 'Everyday', 'IN_PROGRESS', '2023-12-20', '2023-12-20', '2023-12-21 02:40:00'),
('59118012440636', '80593236', 'jogging', 'Weekly', 'Tuesday Friday Sunday', 'IN_PROGRESS', '2024-01-12', '2024-01-12', '2024-01-12 13:50:18'),
('64033732316412', '77751626', 'gym', 'Daily', 'Everyday', 'IN_PROGRESS', '2024-03-19', '2024-03-19', '2024-03-19 21:58:48'),
('64895206698560', '40993249', 'drive a bike', 'Daily', 'Everyday', 'IN_PROGRESS', '2023-12-18', '2023-12-18', '2023-12-21 02:40:00'),
('69574406644785', '40993249', 'read java', 'Daily', 'Everyday', 'IN_PROGRESS', '2023-12-20', '2023-12-20', '2023-12-21 02:40:00'),
('69928045660556', '40993249', 'Take some coffee', 'Daily', 'Everyday', 'IN_PROGRESS', '2023-12-19', '2023-12-19', '2023-12-21 02:40:00'),
('90842994913069', '77387001', 'lawn the field', 'Weekly', 'Wednesday Thursday Saturday Friday', 'IN_PROGRESS', '2023-11-30', '2023-12-13', '2023-12-21 02:40:00'),
('98275512898558', '52166444', 'Read Chemistry', 'Weekly', 'Friday Saturday', 'STOPPED', '2020-02-17', '2023-03-13', '2023-12-21 02:40:00');

-- --------------------------------------------------------

--
-- Table structure for table `userz`
--

CREATE TABLE `userz` (
  `user_id` varchar(8) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `pazzword` varchar(50) DEFAULT NULL,
  `user_name` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userz`
--

INSERT INTO `userz` (`user_id`, `email`, `pazzword`, `user_name`) VALUES
('40993249', 'efe@gmail.com', 'efe', 'efe'),
('52166444', 'gabreilla@gmail.com', 'gabriel', 'gabi'),
('77387001', 'maryjane@gmail.com', 'janey', 'maryjane'),
('77751626', 'sundayonojaife@gmail.com', 'powerful123', 'sunday_mamuyowi.onojaife'),
('80593236', 'sunday@gmail.com', 'sunday', 'sunday'),
('84615070', 'karpov@gmail.com', 'karpov', 'karpov'),
('99899074', 'johndoe@gmail.com', 'johnny', 'johndoe');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `completed_habits`
--
ALTER TABLE `completed_habits`
  ADD PRIMARY KEY (`complete_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `habit_id` (`habit_id`);

--
-- Indexes for table `habit`
--
ALTER TABLE `habit`
  ADD PRIMARY KEY (`habit_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `userz`
--
ALTER TABLE `userz`
  ADD PRIMARY KEY (`user_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `completed_habits`
--
ALTER TABLE `completed_habits`
  ADD CONSTRAINT `completed_habits_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `userz` (`user_id`),
  ADD CONSTRAINT `completed_habits_ibfk_2` FOREIGN KEY (`habit_id`) REFERENCES `habit` (`habit_id`);

--
-- Constraints for table `habit`
--
ALTER TABLE `habit`
  ADD CONSTRAINT `habit_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `userz` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
