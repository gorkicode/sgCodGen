package com.example.crudwithvaadin;

import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.grid.Grid;
import com.vaadin.flow.component.icon.VaadinIcon;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.data.value.ValueChangeMode;
import com.vaadin.flow.router.Route;
import org.springframework.util.StringUtils;

@Route
public class MainView extends VerticalLayout {

	private final <*E>Repository repo;

	private final <*E>Editor editor;

	final Grid<<*E>> grid;

	final TextField filter;

	private final Button addNewBtn;

	public MainView(<*E>Repository repo, <*E>Editor editor) {
		this.repo = repo;
		this.editor = editor;
		this.grid = new Grid<>(<*E>.class);
		this.filter = new TextField();
		this.addNewBtn = new Button("New <*e>", VaadinIcon.PLUS.create());

		// build layout
		HorizontalLayout actions = new HorizontalLayout(filter, addNewBtn);
		add(actions, grid, editor);

		grid.setHeight("300px");
		grid.setColumns("id", "firstName", "lastName");
		grid.getColumnByKey("id").setWidth("50px").setFlexGrow(0);

		filter.setPlaceholder("Filter by last name");

		// Hook logic to components

		// Replace listing with filtered content when user changes filter
		filter.setValueChangeMode(ValueChangeMode.LAZY);
		filter.addValueChangeListener(e -> list<*E>s(e.getValue()));

		// Connect selected <*E> to editor or hide if none is selected
		grid.asSingleSelect().addValueChangeListener(e -> {
			editor.edit<*E>(e.getValue());
		});

		// Instantiate and edit new <*E> the new button is clicked
		addNewBtn.addClickListener(e -> editor.edit<*E>(new <*E>("", "")));

		// Listen changes made by the editor, refresh data from backend
		editor.setChangeHandler(() -> {
			editor.setVisible(false);
			list<*E>s(filter.getValue());
		});

		// Initialize listing
		list<*E>s(null);
	}

	// tag::list<*E>[]
	void list<*E>s(String filterText) {
		if (StringUtils.hasText(filterText)) {
			grid.setItems(repo.findByLastNameStartsWithIgnoreCase(filterText));
		} else {
			grid.setItems(repo.findAll());
		}
	}
	// end::list<*E>[]

}
