DELETE FROM `Metals`;
DELETE FROM `Sizes`;
DELETE FROM `Styles`;
DELETE FROM `Orders`;

DROP TABLE IF EXISTS `Metals`;
DROP TABLE IF EXISTS `Sizes`;
DROP TABLE IF EXISTS `Styles`;
DROP TABLE IF EXISTS `Orders`;


-- Create tables
CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(6,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(3, 2) NOT NULL,
    `price` NUMERIC(6, 2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(100) NOT NULL,
    `price` NUMERIC (6, 2)
);

CREATE TABLE `Orders` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `created_at`    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `metal_id`  INT NOT NULL,
    `size_id` INT NOT NULL,
    `style_id` INT NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

-- Insert records into tables
INSERT INTO `Metals` VALUES (null, 'Sterling Silver', 12.42);
INSERT INTO `Metals` VALUES (null, '14K Gold', 736.40);
INSERT INTO `Metals` VALUES (null, '24K Gold', 1258.90);
INSERT INTO `Metals` VALUES (null, 'Platinum', 795.45);
INSERT INTO `Metals` VALUES (null, 'Palladium', 1241);

INSERT INTO `Sizes` VALUES(null, 0.5, 405);
INSERT INTO `Sizes` VALUES(null, 0.75, 782);
INSERT INTO `Sizes` VALUES(null, 1, 1470);
INSERT INTO `Sizes` VALUES(null, 1.5, 1997);
INSERT INTO `Sizes` VALUES(null, 2, 3638);

INSERT INTO "Styles" VALUES(null, 'Classic', 500);
INSERT INTO "Styles" VALUES(null, 'Modern', 710);
INSERT INTO "Styles" VALUES(null, 'Vintage', 965);

INSERT INTO `Orders`(metal_id, size_id, style_id) VALUES(1, 1, 1);
INSERT INTO `Orders`(created_at, metal_id, size_id, style_id) VALUES(CURRENT_TIMESTAMP, 2, 5, 3);
INSERT INTO `Orders`(metal_id, size_id, style_id) VALUES(4, 2, 1);