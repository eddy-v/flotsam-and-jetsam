DROP TABLE IF EXISTS supbowl;

CREATE TABLE supbowl
(
  bowlnbr int(3),
  year int(4), 
  romannbr varchar(8),
  winner varchar(12),
  wscore int(3),
  loser varchar(12),
  losescore int(3),
  conf char(1),
  djprior float(10.2),
  djyearend float(10.2)
  );
