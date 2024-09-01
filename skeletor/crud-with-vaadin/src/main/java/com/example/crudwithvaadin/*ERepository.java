package com.example.crudwithvaadin;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface <*E>Repository extends JpaRepository<<*E>, Long> {

	List<<*E>> findByLastNameStartsWithIgnoreCase(String lastName);
}
