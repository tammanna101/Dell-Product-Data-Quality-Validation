-- Validation Summary

SELECT
    Validation_Status,
    COUNT(*) AS Total_Records
FROM Product_Validation
GROUP BY Validation_Status;


-- Missing Attribute Analysis

SELECT
    Attribute_Name,
    COUNT(*) AS Missing_Count
FROM Product_Validation
WHERE Source_Value IS NULL
   OR Source_Value = 'NA'
GROUP BY Attribute_Name
ORDER BY Missing_Count DESC;


-- Product Not Found Analysis

SELECT
    Item_Class,
    Attribute_Name,
    COUNT(*) AS Not_Found_Count
FROM Product_Validation
WHERE Validation_Status = 'Not Found'
GROUP BY Item_Class, Attribute_Name
ORDER BY Not_Found_Count DESC;


-- Success Percentage

SELECT
    ROUND(
        100.0 *
        SUM(CASE WHEN Validation_Status='Valid' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Validation_Success_Percentage
FROM Product_Validation;
