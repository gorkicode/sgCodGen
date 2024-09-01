package com.example.crudwithvaadin;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class CrudWithVaadinApplication {

	private static final Logger log = LoggerFactory.getLogger(CrudWithVaadinApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(CrudWithVaadinApplication.class);
	}

	@Bean
	public CommandLineRunner loadData(<*E>Repository repository) {
		return (args) -> {
			// save a couple of <*e>
			repository.save(new <*E>("Jack", "Bauer"));
			repository.save(new <*E>("Chloe", "O'Brian"));
			repository.save(new <*E>("Kim", "Bauer"));
			repository.save(new <*E>("David", "Palmer"));
			repository.save(new <*E>("Michelle", "Dessler"));

			// fetch all <*e>
			log.info("<*E>s found with findAll():");
			log.info("-------------------------------");
			for (<*E> <*e> : repository.findAll()) {
				log.info(<*e>.toString());
			}
			log.info("");

			// fetch an individual <*e> by ID
			<*E> <*e> = repository.findById(1L).get();
			log.info("<*E> found with findOne(1L):");
			log.info("--------------------------------");
			log.info(<*e>.toString());
			log.info("");

			// fetch <*e>s by last name
			log.info("<*E> found with findByLastNameStartsWithIgnoreCase('Bauer'):");
			log.info("--------------------------------------------");
			for (<*E> bauer : repository
					.findByLastNameStartsWithIgnoreCase("Bauer")) {
				log.info(bauer.toString());
			}
			log.info("");
		};
	}

}
