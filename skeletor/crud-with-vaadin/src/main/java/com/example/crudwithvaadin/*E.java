package com.example.crudwithvaadin;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
public class <*E> {

	@Id
	@GeneratedValue
	private Long id;

	private String firstName;

	private String lastName;

	protected <*E>() {
	}

	public <*E>(String firstName, String lastName) {
		this.firstName = firstName;
		this.lastName = lastName;
	}

	public Long getId() {
		return id;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	@Override
	public String toString() {
		return String.format("<*E>[id=%d, firstName='%s', lastName='%s']", id,
				firstName, lastName);
	}

}
