create table questions ( author varchar(30) not null, qid bigint primary key, explanation varchar(100), body varchar(100) not null, time timestamp not null, authorid bigint not null);

CREATE TABLE `answers` (
  `author` varchar(30) NOT NULL,
  `answerid` bigint(20) NOT NULL,
  `body` varchar(100) DEFAULT NULL,
  `timeofpost` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `quesid` bigint(20) NOT NULL,
  `authid` bigint(20) NOT NULL,
  PRIMARY KEY (`answerid`),
  KEY `fk11` (`quesid`),
  CONSTRAINT `fk11` FOREIGN KEY (`quesid`) REFERENCES `questions` (`qid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

 CREATE TABLE `user` (
  `name` varchar(30) NOT NULL,
  `loginemail` varchar(30) NOT NULL,
  `password` varchar(10) NOT NULL,
  `numfollowers` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`loginemail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `comments` (
  `author` varchar(30) NOT NULL,
  `commentid` bigint(20) NOT NULL,
  `timeofcomment` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `authorid` varchar(30) NOT NULL,
  `ansid` bigint(20) NOT NULL,
  PRIMARY KEY (`commentid`),
  KEY `fk21` (`authorid`),
  KEY `fk22` (`ansid`),
  CONSTRAINT `fk21` FOREIGN KEY (`authorid`) REFERENCES `user` (`loginemail`),
  CONSTRAINT `fk22` FOREIGN KEY (`ansid`) REFERENCES `answers` (`answerid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `topic` (
  `topicid` bigint(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`topicid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `question_topic` (
  `quesid` bigint(20) NOT NULL,
  `topicid` bigint(20) NOT NULL,
  `qtid` bigint(20) NOT NULL,
  PRIMARY KEY (`qtid`),
  KEY `fk01` (`quesid`),
  KEY `fk02` (`topicid`),
  CONSTRAINT `fk01` FOREIGN KEY (`quesid`) REFERENCES `questions` (`qid`),
  CONSTRAINT `fk02` FOREIGN KEY (`topicid`) REFERENCES `topic` (`topicid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `user_follow_question` (
  `userid` varchar(30) NOT NULL,
  `qid` bigint(20) NOT NULL,
  `ufqid` bigint(20) NOT NULL,
  PRIMARY KEY (`ufqid`),
  KEY `fk1` (`userid`),
  KEY `fk2` (`qid`),
  CONSTRAINT `fk1` FOREIGN KEY (`userid`) REFERENCES `user` (`loginemail`),
  CONSTRAINT `fk2` FOREIGN KEY (`qid`) REFERENCES `questions` (`qid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `user_fav_question` (
  `userid` varchar(30) NOT NULL,
  `qid` bigint(20) NOT NULL,
  `ufqid` bigint(20) NOT NULL,
  PRIMARY KEY (`ufqid`),
  KEY `fk10` (`userid`),
  KEY `fk20` (`qid`),
  CONSTRAINT `fk10` FOREIGN KEY (`userid`) REFERENCES `user` (`loginemail`),
  CONSTRAINT `fk20` FOREIGN KEY (`qid`) REFERENCES `questions` (`qid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `user_follow_user` (
  `follower_id` varchar(30) NOT NULL,
  `followed_id` varchar(30) NOT NULL,
  `ufuid` bigint(20) NOT NULL,
  PRIMARY KEY (`ufuid`),
  KEY `fk03` (`follower_id`),
  KEY `fk04` (`followed_id`),
  CONSTRAINT `fk03` FOREIGN KEY (`follower_id`) REFERENCES `user` (`loginemail`),
  CONSTRAINT `fk04` FOREIGN KEY (`followed_id`) REFERENCES `user` (`loginemail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `user_can_upvote` (
  `user_id` varchar(30) NOT NULL,
  `ans_id` bigint(20) NOT NULL,
  `ucuid` bigint(20) NOT NULL,
  PRIMARY KEY (`ucuid`),
  KEY `fk05` (`user_id`),
  KEY `fk06` (`ans_id`),
  CONSTRAINT `fk05` FOREIGN KEY (`user_id`) REFERENCES `user` (`loginemail`),
  CONSTRAINT `fk06` FOREIGN KEY (`ans_id`) REFERENCES `answers` (`answerid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin;

CREATE TABLE `user_follow_topic` (
  `user_id` varchar(30) NOT NULL,
  `topic_id` bigint(20) NOT NULL,
  `uftid` bigint(20) NOT NULL,
  PRIMARY KEY (`uftid`),
  KEY `fk07` (`user_id`),
  KEY `fk08` (`topic_id`),
  CONSTRAINT `fk07` FOREIGN KEY (`user_id`) REFERENCES `user` (`loginemail`),
  CONSTRAINT `fk08` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`topicid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `user_fav_answer` (
  `userid` varchar(30) NOT NULL,
  `ansid` bigint(20) NOT NULL,
  `ufaid` bigint(20) NOT NULL,
  PRIMARY KEY (`ufaid`),
  KEY `fk101` (`userid`),
  KEY `fk09` (`ansid`),
  CONSTRAINT `fk101` FOREIGN KEY (`userid`) REFERENCES `user` (`loginemail`),
  CONSTRAINT `fk09` FOREIGN KEY (`ansid`) REFERENCES `answers` (`answerid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
