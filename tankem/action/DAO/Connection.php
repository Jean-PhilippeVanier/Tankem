<?php
	class Connection {
		private static $connection;

		public static function getConnection() {
			if (Connection::$connection == null) {
				Connection::$connection = new PDO("oci:dbname=DECINFO", "e1384492", "C");
				Connection::$connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
				Connection::$connection->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
			}

			return Connection::$connection;
		}

		public static function closeConnection() {
			Connection::$connection = null;
		}

	}
